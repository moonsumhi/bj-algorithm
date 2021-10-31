import json
from collections import defaultdict

N = 5
INIT_BIKE_NUM = 4
AVG_BIKE_REQ = 2
ENOUGH_BIKE_NUM = INIT_BIKE_NUM - AVG_BIKE_REQ + 1
LACKING_BIKE_NUM = INIT_BIKE_NUM - AVG_BIKE_REQ - 1
TRUCK_NUM = 5
ID_DICT = {}
TPM = 6
TPL = 6
MAX_BIKE = 20
THRESHOLD = 8
Board = [[] for _ in range(N)]
Trucks = []
Returns = defaultdict(list)

class Truck:
    def __init__(self, id, row, col, bike):
        self.id = id
        self.row = row
        self.col = col
        self.bike = bike
        self.cost = 60/TPM


class Node:
    def __init__(self, id, row, col):
        self.id = id
        self.row = row
        self.col = col
        self.bike = INIT_BIKE_NUM
        ID_DICT[id] = [row, col]

def print_bikes():
    for i in range(N):
        for j in range(N):
            print(Board[i][j].bike, end=' ')
        print()


def searching(p1, p2):
    # p1: Truck, Node / p2: Node
    booked = {}
    # search bikes by nearest id
    for i in p1:
        p1_id = i.id
        p1_row = i.row
        p1_col = i.col
        dist = []
        for j in p2:
            p2_id = j.id
            p2_row = j.row
            p2_col = j.col
            if p2_id in booked.values():
                continue
            dist.append((abs(p1_row-p2_row) + abs(p1_col-p2_col), p2_id))
        # print("i : ", i.id, i.row, i.col)
        #
        # print("dist : ", dist)
        if dist:
            # p1_id, p2_id
            booked[p1_id] = min(dist)[1]
    # print("booked: ", booked)

    return booked


def check_cost(t_id, f_id, p1, p2):

    # print("t_id, f_id : ", t_id, f_id)
    # print("trucks row, col ", Trucks[t_id].row, Trucks[t_id].col)
    # print("trucks row, col ", p1[t_id].row, p1[t_id].col)

    p1_row, p1_col = p1[t_id].row, p1[t_id].col
    p2_row, p2_col = ID_DICT[f_id]

    # 1 min, go to station
    if (abs(p1_row - p2_row) + abs(p1_col - p2_col)) <= THRESHOLD:
        p1[t_id].cost -= (abs(p1_row - p2_row) + abs(p1_col - p2_col))
        p1[t_id].row, p1[t_id].col = p2_row, p2_col
    else:
        return False

    return True


def truck_move(empty_b, full_b):

    print("========Before============")
    print_bikes()
    # searching, matching
    t_to_full = searching(Trucks, full_b)
    full_b_nodes = []
    for f_b in t_to_full.values():
        row, col = ID_DICT[f_b]
        full_b_nodes.append(Board[row][col])
    f_to_empty = searching(full_b_nodes, empty_b)

    print(t_to_full)
    print(f_to_empty)

    # loading
    for t_id, f_id in t_to_full.items():
        if not check_cost(t_id, f_id, Trucks, ID_DICT):
            continue

        if Trucks[t_id].cost > 0:
            Trucks[t_id].cost -= 1
            Trucks[t_id].bike += 1
            Board[Trucks[t_id].row][Trucks[t_id].col].bike -= 1
        else:
            continue

    print("========AfterLoading============")
    print_bikes()

    t_to_empty = {}
    for t_id, f_id in t_to_full.items():
        if f_id in f_to_empty:
            t_to_empty[t_id] = f_to_empty[f_id]
        else:
            # restore bikes
            Trucks[t_id].bike -= 1
            Board[Trucks[t_id].row][Trucks[t_id].col].bike += 1


    # unloading
    for t_id, e_id in t_to_empty.items():

        if not check_cost(t_id, e_id, Trucks, ID_DICT):
            # restore bikes
            Trucks[t_id].bike -= 1
            Board[Trucks[t_id].row][Trucks[t_id].col].bike += 1
            continue

        if Trucks[t_id].cost > 0:
            print("**bike updates")
            Trucks[t_id].cost -= 1
            Trucks[t_id].bike -= 1
            Board[Trucks[t_id].row][Trucks[t_id].col].bike += 1
        else:
            continue

    print("========After unloading============")
    print_bikes()


def solution():

    # read data
    with open('day1.json') as json_file:
        json_data = json.load(json_file)

    # init board
    for i in range(N):
        for j in range(N):
            Board[i].append(Node((N - 1) - i + (N * j), i, j))


    # init trucks
    for i in range(TRUCK_NUM):
        Trucks.append(Truck(i, 4, 0, 0))

    print(json_data)
    # [자전거를 대여할 자전거 대여소 ID, 자전거를 반납할 자전거 대여소 ID, 자전거를 탈 시간(분)]
    for i in range(100):

        time = str(i)
        if time not in json_data:
            continue

        # return
        for r_id in Returns.keys():
            for r_idx in range(len(Returns[r_id])):
                Returns[r_id][r_idx] -= 1
                if Returns[r_id][r_idx] == 0:
                    print("@@@@@@@@@Before return@@@@@@@@@")
                    print_bikes()
                    r_row, r_col = ID_DICT[r_id]
                    Board[r_row][r_col].bike += 1
                    print("@@@@@@@@@After return@@@@@@@@@@")
                    print("curr_time = ", i)
                    print_bikes()
            Returns[r_id] = list(filter(lambda a: a != 0, Returns[r_id]))

        # init turck's cost
        for truck in Trucks:
            truck.cost = 60 / TPM

        succss = 0
        for req in json_data[time]:
            bor_id, ret_id, bike_time = req
            bor_row, bor_col = ID_DICT[bor_id]
            Returns[ret_id].append(bike_time)

            if Board[bor_row][bor_col].bike > 0:
                succss += 1
                Board[bor_row][bor_col].bike -= 1

        empty_b = []
        full_b = []
        for i in range(N):
            for j in range(N):
                if Board[i][j].bike >= ENOUGH_BIKE_NUM:
                    full_b.append(Board[i][j])
                if Board[i][j].bike <= LACKING_BIKE_NUM:
                    empty_b.append(Board[i][j])

        if empty_b:
            truck_move(empty_b, full_b)


solution()









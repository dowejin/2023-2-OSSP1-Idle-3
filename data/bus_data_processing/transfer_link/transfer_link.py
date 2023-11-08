import json

# LOGIC
# 1. 버스 정류장 데이터에서 하나의 노드(정류장)씩 뽑아서 
#   해당 정류장의 id가 출발지 혹은 도착지에 들어있는 버스노선 들을 찾고 route_id 별로 묶는다.
# 2. 찾은 버스노선의 갯수만큼 버스 노드를 생성해준다. 
# 3. 생성된 버스 노드 id를 이용하여 엣지의 기존 출발지 혹은 도착지 id를 수정해준다.
# 4. 위 과정을 통해 새로운 버스 노드와 엣지가 생성된다. 기존의 버스 노드와 엣지는 사용하지 않는다.
# 5. 이때 생성된 각각의 버스 노드들끼리 연결하는 엣지를 생성해준다.(환승 엣지로 사용될 것이다.)

# 적어놓기
# 기존 버스 정류장 노드의 id 범위는 100000001 ~ 717104358


def generateTransferBusNode():

    bus_stop_node_with_transfer_index = 1000000001
    
    # 각각의 노선별로 나눠진 정류장 노드가 들어가게 되는 새로운 버스 정류장 노드 
    bus_stop_node_with_transfer = []

    # 새로운 버스 정류장 노드가 적용된 엣지
    bus_route_edge_with_transfer = []

    bus_stop_filePath = 'bus_stop_node.json'
    bus_route_filePath = 'bus_router_edge.json'

    with open(bus_stop_filePath, 'r', encoding='utf-8') as f:
        bus_stop_list = json.load(f)

    with open(bus_route_filePath, 'r', encoding='utf-8') as f:
        bus_route_list = json.load(f)   

    for bus_stop in bus_stop_list:
        bus_stop_id = bus_stop['id']

        # 해당 정류장의 id가 출발지 혹은 도착지에 들어있는 버스노선 들을 찾고 route_id 별로 묶는다
        bus_route_group = {}
        for bus_route in bus_route_list:
            if bus_stop_id == bus_route['start'] or bus_stop_id == bus_route['end']:
                if bus_route['route_id'] not in bus_route_group:
                    bus_route_group[bus_route['route_id']] = []
                bus_route_group[bus_route['route_id']].append(bus_route)

            # 찾은 버스노선의 갯수만큼 버스 노드를 생성해준다. 
            for route_id, bus_routes in bus_route_group.items():
                bus_stop_node_with_transfer.append({
                    "id" : bus_stop_node_with_transfer_index,
                    "position" : {
                        "latitude" : bus_stop['position']['latitude'],
                        "longitude" : bus_stop['position']['longitude'],
                    },
                    "name" : bus_stop['name'] + "_" + bus_route['line'],
                })

                #생성된 버스 노드 id를 이용하여 엣지의 기존 출발지 혹은 도착지 id를 수정해준다.
                for bus_route in bus_routes:
                    if bus_stop_id == bus_route['start']:
                        bus_route['start'] = bus_stop_node_with_transfer_index
                    elif bus_stop_id == bus_route['end']:
                        bus_route['end'] = bus_stop_node_with_transfer_index

                    # 수정된 엣지를 새로운 엣지 리스트에 추가해준다.
                    bus_route_edge_with_transfer.append(bus_route)

                bus_stop_node_with_transfer_index += 1

    
    with open('bus_stop_node_with_transfer.json', 'w', encoding='utf-8') as f:
        json.dump(bus_stop_node_with_transfer, f, indent=4, ensure_ascii=False)

    with open('bus_route_edge_with_transfer.json', 'w', encoding='utf-8') as f:
        json.dump(bus_route_edge_with_transfer, f, indent=4, ensure_ascii=False)


def generateTransferBusEdge():
    pass


generateTransferBusNode()
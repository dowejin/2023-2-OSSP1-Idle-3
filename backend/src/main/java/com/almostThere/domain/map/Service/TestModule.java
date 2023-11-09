package com.almostThere.domain.map.Service;

import com.almostThere.domain.map.Service.router.Router;
import com.almostThere.domain.map.Service.router.impl.DiRouter;
import com.almostThere.domain.map.entity.link.MapLink;
import com.almostThere.domain.map.entity.node.MapNode;
import com.almostThere.domain.map.repository.graphBuilder.MapGraphBuilder;
import com.almostThere.domain.map.repository.graphBuilder.impl.ListMapGraphBuilder;
import com.almostThere.domain.map.repository.graphLoader.GRAPH_FILE;
import com.almostThere.domain.map.repository.graphLoader.GraphLoader;
import com.almostThere.domain.map.repository.graphLoader.impl.JSONGraphLoader;
import com.almostThere.domain.map.repository.mapGraph.MapGraph;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import org.json.simple.parser.ParseException;

public class TestModule {
    public static void main(String[] args) throws IOException, ParseException {
        GraphLoader graphLoader = new JSONGraphLoader();
        MapGraphBuilder graphBuilder = new ListMapGraphBuilder();

        List<GRAPH_FILE> nodeFiles = List.of(
            GRAPH_FILE.SUBWAY_NODE,
            GRAPH_FILE.STEP_NODE,
            GRAPH_FILE.BUS_STOP_NODE
        );
        List<GRAPH_FILE> edgeFiles = List.of(
            GRAPH_FILE.SUBWAY_EDGE,
            GRAPH_FILE.STEP_EDGE,
            GRAPH_FILE.BUS_ROUTER_EDGE,
            GRAPH_FILE.SUBWAY_STEP_EDGE
        );
        List<MapNode> map_nodes = new ArrayList<>();
        List<MapLink> map_edges = new ArrayList<>();
        for (GRAPH_FILE nodeFile : nodeFiles) {
            map_nodes.addAll(graphLoader.loadNodes(nodeFile));
        }
        for (GRAPH_FILE edgeFile : edgeFiles) {
            System.out.println(edgeFile.getName());
            map_edges.addAll(graphLoader.loadEdges(edgeFile));
        }
        MapGraph mapGraph = graphBuilder.build(map_nodes, map_edges);
        Router diRouter = null;

        Scanner scanner = new Scanner(System.in); // 콘솔 입력을 위한 Scanner 생성
        try {
            System.out.println("Enter a source number :");
            if (scanner.hasNextLong()) { // long 값이 입력될 때까지 기다림
                long srcMapId = scanner.nextLong();
                if (srcMapId < 0) return;

                long beforeTime = System.currentTimeMillis();
                int searchId = mapGraph.findSearchId(srcMapId);
                diRouter = new DiRouter(mapGraph.getNodeNum(), searchId, mapGraph);
                long afterTime = System.currentTimeMillis();
                long diffTime = afterTime - beforeTime;
                System.out.println("실행 시간(ms): " + diffTime);
                diRouter.getShortestPath();
                // 입력받은 값으로 작업 수행, 예를 들어 최단 경로 계산 등

                System.out.println("You entered: " + srcMapId);
            } else {
                // 입력된 값이 long이 아닐 경우
                System.out.println("Invalid input. Please enter a number.");
                return ;
            }

            System.out.println("Enter a destination number: ");
            while (true) {
                if (scanner.hasNextLong()) { // long 값이 입력될 때까지 기다림
                    long mapId = scanner.nextLong();
                    if (mapId == -1) {
                        System.out.println("Exiting program.");
                        break;
                    }
                    // 입력받은 값으로 작업 수행, 예를 들어 최단 경로 계산 등

                    System.out.println("You entered: " + mapId);
                    diRouter.showPath(mapId);
                    System.out.println("Enter another number or -1 to exit: ");
                } else {
                    // 입력된 값이 long이 아닐 경우
                    System.out.println("Invalid input. Please enter a number.");
                    scanner.next(); // 현재 입력을 소비하여 다음 입력을 기다림
                }
            }
        } finally {
            scanner.close(); // Scanner 인스턴스를 닫아 자원을 해제
        }
    }
}

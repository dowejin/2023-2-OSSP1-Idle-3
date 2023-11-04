package com.almostThere.domain.map.repository.mapGraphConfig;

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
import org.json.simple.parser.ParseException;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MapGraphConfig {

    @Bean
    public MapGraph mapGraph() throws IOException, ParseException {
        GraphLoader graphLoader = new JSONGraphLoader();
        MapGraphBuilder graphBuilder = new ListMapGraphBuilder();

        List<GRAPH_FILE> nodeFiles = List.of(GRAPH_FILE.SUBWAY_NODE, GRAPH_FILE.STEP_NODE, GRAPH_FILE.BUS_STOP_NODE);
        List<GRAPH_FILE> edgeFiles = List.of(GRAPH_FILE.SUBWAY_EDGE, GRAPH_FILE.STEP_EDGE, GRAPH_FILE.BUS_ROUTER_EDGE);
        List<MapNode> map_nodes = new ArrayList<>();
        List<MapLink> map_edges = new ArrayList<>();
        for (GRAPH_FILE nodeFile : nodeFiles) {
            map_nodes.addAll(graphLoader.loadNodes(nodeFile));
        }
        for (GRAPH_FILE edgeFile : edgeFiles) {
            map_edges.addAll(graphLoader.loadEdges(edgeFile));
        }
        return graphBuilder.build(map_nodes, map_edges);
    }
}

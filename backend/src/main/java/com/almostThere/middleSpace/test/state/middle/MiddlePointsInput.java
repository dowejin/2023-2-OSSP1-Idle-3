package com.almostThere.middleSpace.test.state.middle;

import com.almostThere.middleSpace.test.state.TestState;
import com.almostThere.middleSpace.test.context.middle.MiddleContext;
import java.util.Scanner;
import lombok.RequiredArgsConstructor;
import org.springframework.data.geo.Point;

/**
 * 중간 지점 선정 알고리즘을 위한 입력을 받는 State
 */
@RequiredArgsConstructor
public class MiddlePointsInput implements TestState {
    private final MiddleContext context;
    @Override
    public void action() {
        System.out.print("출발점의 개수를 입력하세요 : ");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        if (n < 0) {
            System.exit(0);
        }
        System.out.printf("%d 개의 출발점의 위도 경도를 입력하세요 :\n", n);
        for (int i = 0 ; i < n ; i++) {
            double lat = scanner.nextDouble(); // 위도 y,
            double log = scanner.nextDouble(); // 경도 x
            this.context.getInputPoints().add(new Point(log, lat));
        }
        this.context.setState("GetMiddle");
    }
}

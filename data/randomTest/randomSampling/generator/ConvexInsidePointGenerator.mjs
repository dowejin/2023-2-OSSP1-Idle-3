import OvalConvexPointsGenerater from "./OvalConvexPointsGenerater.mjs";
import InsidePointsGenerator from "./InsidePointsGenerator.mjs";

export default class ConvexInsidePointGenerator {
    constructor(minLat, maxLat, minLng, maxLng) {
        // 위도 범위
        this.minLat = minLat;
        this.maxLat = maxLat;
        // 경도 범위
        this.minLng = minLng;
        this.maxLng = maxLng;
        // 볼록다각형과 그 안에 점을 생성하는 생성기
        this.polygonSupplier = new OvalConvexPointsGenerater();
        this.insideDotSupplier = new InsidePointsGenerator();
    }

    /**
     * @param {number} n : n각형의 n 
     * @param {number} insideDotNumber : 내부 점의 개수
     * @Param (number) tryNumber : 랜덤 시도 횟수
     */
    generate(n, insideDotNumber, tryNumber = 1000) {
        const minLocalLat = this.getRandomBetween(this.minLat, this.maxLat)
        const maxLocalLat = this.getRandomBetween(minLocalLat, this.maxLat)

        const minLocalLng = this.getRandomBetween(this.minLng, this.maxLng)
        const maxLocalLng = this.getRandomBetween(minLocalLng, this.maxLng)

        const polygon = this.polygonSupplier.generate(n, minLocalLat, maxLocalLat, minLocalLng, maxLocalLng);
        const inside = this.insideDotSupplier.generate(polygon, insideDotNumber, tryNumber);
        return [...polygon, ...inside];
    }

    getRandomBetween(min, max){
        return Math.random() * (max - min) + min;
    }
};
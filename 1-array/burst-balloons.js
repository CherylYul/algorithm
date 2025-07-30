/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
  points.sort((pointA, pointB) => pointA[0] - pointB[0])
  let overlappingEnd = points[0][1]
  let arrow = 1
  for (let i=1; i < points.length; i++) {
    if (points[i][0] <= overlappingEnd) {
        overlappingEnd = Math.min(overlappingEnd, points[i][1])
    } else {
        arrow++;
        overlappingEnd = points[i][1]
    }
  }
  return arrow;
};
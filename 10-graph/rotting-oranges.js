/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    const row = grid.length
    const col = grid[0].length
    let orange = 0
    let rottenOranges = []
    for (let r=0; r<row; r++) {
        for (let c=0; c<col; c++) {
            if (grid[r][c] === 2) rottenOranges.push([r,c])
            if (grid[r][c] !== 0) orange++
        }
    }
    if (orange === 0 || orange === rottenOranges.length) return 0
    if (rottenOranges.length === 0) return -1
    
    let minute = 0
    const directions = [[0,1],[0,-1],[1,0],[-1,0]]
    let q = [rottenOranges]
    let rottenNums = rottenOranges.length
    while (q.length > 0) {
        const thisTime = q.shift()
        let nextTime = []
        for (const coor of thisTime) {
            for (const d of directions) {
                const r = coor[0] + d[0]
                const c = coor[1] + d[1]
                if (r>=0 && r<row && c>=0 && c<col && grid[r][c] === 1) {
                    nextTime.push([r,c])
                    grid[r][c] = 2
                    rottenNums++
                }
            }
        }
        if (nextTime.length > 0) {
            minute++
            q.push(nextTime)
        }
    }
    
    if (rottenNums < orange) return -1
    return minute
};
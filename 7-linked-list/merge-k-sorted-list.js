/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

var mergeKLists = function(lists) {
    if (!lists || !lists.length) return null
    while (lists.length > 1) {
        let mergedList = new Array()
        for (let i=0; i<lists.length; i+=2) {
            let l1 = lists[i]
            let l2 = i+1 < lists.length ? lists[i+1]:null
            mergedList.push(mergeLists(l1,l2))
        }
        lists = mergedList
    }
    return lists[0]
};

var mergeLists = function(l1,l2) {
    let dummy = new ListNode()
    let curr = dummy
    while (l1 && l2) {
        if (l1.val <= l2.val) {
            curr.next = l1
            l1 = l1.next
        } else {
            curr.next = l2
            l2 = l2.next
        }
        curr = curr.next
    }
    curr.next = l1 ? l1 : l2
    return dummy.next
}

// var mergeKLists = function(lists) {
//     const hashMap = {}
//     for (const list of lists) {
//         let curr = list
//         while (curr) {
//             hashMap[curr.val] = (hashMap[curr.val] || 0) + 1
//             curr = curr.next
//         }
//     }
//     const sortedHashMap = Object.keys(hashMap).sort((a,b)=>a-b)
//     let dummy = new ListNode(-1)
//     let curr = dummy
//     for (const num of sortedHashMap) {
//         for (let i=0; i<hashMap[num]; i++) {
//             curr.next = new ListNode(Number(num))
//             curr = curr.next
//         }
//     }
//     return dummy.next
// };
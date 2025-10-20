class Solution {
    // counter
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] counter = new int[26];
        for (int i=0; i<s.length(); i++) {
            counter[s.charAt(i) - 'a']++;
        }
        for (int i=0; i<t.length(); i++) {
            if (counter[t.charAt(i) - 'a'] == 0) return false;
            counter[t.charAt(i) - 'a']--;
        }
        return true;
    }

    // hashmap
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        Map<Character,Integer> hashTable = new HashMap<>();
        for (int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            hashTable.put(ch, hashTable.getOrDefault(ch, 0)+1);
        }
        for (int i=0; i<t.length(); i++) {
            char ch = t.charAt(i);
            if (!hashTable.containsKey(ch) || hashTable.get(ch) == 0) {
                return false;
            }
            hashTable.put(ch, hashTable.get(ch)-1);
        }
        return true;
    }

    // sorting
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        Arrays.sort(sArray);
        Arrays.sort(tArray);
        return Arrays.equals(sArray, tArray);
    }
}
class Solution {
   public List<String> readBinaryWatch(int num) {
        List<String> veces = new ArrayList();
        for (int h = 0; h < 12; h++) {
            for (int m = 0; m < 60; m++) {
                if (Integer.bitCount((h << 6) | m) == num) {
                    veces.add(h + ":" + ((m < 10) ? ("0" + m) : m));
                }
            }
        }
        return veces;
    }
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> resultado = new ArrayList<>();
        dfs(root, new StringBuilder(), resultado);
        return resultado;
    }

    private void dfs(TreeNode node, StringBuilder path, List<String> resultado) {
        if (node == null) return;
        int largoArbol = path.length();
        if (largoArbol > 0) {
            path.append("->");
        }
        path.append(node.val);
        if (node.left == null && node.right == null) {
            resultado.add(path.toString());
        } else {
            dfs(node.left, path, resultado);
            dfs(node.right, path, resultado);
        }
        path.setLength(largoArbol);
    }
}

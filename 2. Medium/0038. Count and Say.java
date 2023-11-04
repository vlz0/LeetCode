class Solution {
    public String countAndSay(int n) {
        String valor = "1";
        for (int i = 0 ; i < n-1 ; i++){
            char caracter = valor.charAt(0);
            StringBuilder resultado = new StringBuilder();
            int contador = 1;
            for (int j = 1 ; j < valor.length() ; j++){
                if (caracter != valor.charAt(j)){
                    resultado.append(contador);
                    resultado.append(caracter);
                    contador = 0;
                    caracter = valor.charAt(j);
                }
                contador++;
            }
            resultado.append(contador);
            resultado.append(caracter);
            valor = resultado.toString();
        }
        return valor;
    }
}

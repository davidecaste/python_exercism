class ReverseString {
    String reverse(String inputString) {
        char[] chars = inputString.toCharArray();

        for(int i = 0, j = chars.length - 1; i < j; i++, j--){
            char temp = chars[i];
            chars[i] = chars[j];
            chars[j] = temp;
        }

        return new String(chars);
    }
}

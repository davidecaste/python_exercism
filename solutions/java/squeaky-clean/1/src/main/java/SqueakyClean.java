class SqueakyClean {
    static String clean(String identifier) {
        if (identifier == null) return null;

        char[] asArray = identifier.toCharArray();
        StringBuilder builder = new StringBuilder();
        boolean nextUpper = false; //see if the next char is to capitalize

        for (char c : asArray) {
            switch (c) {
                //task 1
                case ' ':
                case '\t':
                case '\n':
                    builder.append('_');
                    nextUpper = false;
                    break;
                //task 2
                case '-':
                    nextUpper = true;
                    break;
                //task 3
                case '0':
                    builder.append('o');
                    break;
                case '1':
                    builder.append('l');
                    break;
                case '3':
                    builder.append('e');
                    break;
                case '4':
                    builder.append('a');
                    break;
                case '7':
                    builder.append('t');
                    break;
                                    
                default:
                    if (Character.isLetter(c)) { 
                        if (nextUpper) {
                            builder.append(Character.toUpperCase(c));
                            nextUpper = false;
                        } else {
                            builder.append(c);
                        }
                    }
            }
        }

        return builder.toString();
    }
}
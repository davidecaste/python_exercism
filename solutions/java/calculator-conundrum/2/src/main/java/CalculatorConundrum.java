class CalculatorConundrum {
    public String calculate(int operand1, int operand2, String operation) {
        if (operation == null){
            throw new IllegalArgumentException("Operation cannot be null");
        }
        if (operation == ""){
            throw new IllegalArgumentException("Operation cannot be empty");
        }
        int result = 0;
        switch(operation){
            case "+":
                result = operand1 + operand2;
                break;
            case "*":
                result = operand1 * operand2;
                break;
            case "/":
                try{
                    result = operand1 / operand2;
                    break;
                } catch (ArithmeticException e){
                    throw new IllegalOperationException("Division by zero is not allowed", e);
                }
            default:
                throw new IllegalOperationException("Operation '" + operation + "' does not exist");
        }
        return Integer.toString(operand1) + " " + operation + " " + Integer.toString(operand2) + " = " + result;
    }
}

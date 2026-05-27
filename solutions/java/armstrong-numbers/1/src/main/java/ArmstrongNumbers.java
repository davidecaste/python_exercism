class ArmstrongNumbers {

    boolean isArmstrongNumber(int numberToCheck) {
        String stringNumber = String.valueOf(numberToCheck);
        int length = stringNumber.length();
        int sum = 0;
        for (char digit : stringNumber.toCharArray()){
            sum += Math.pow(Character.getNumericValue(digit), length);  
        }
        return numberToCheck == sum;
    }

}

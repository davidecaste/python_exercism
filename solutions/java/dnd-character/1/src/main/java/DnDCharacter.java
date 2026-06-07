import java.util.List;
import java.util.ArrayList;
import java.util.Random;

class DnDCharacter {
    private int constMod;
    private int strength;
    private int dexterity;
    private int constitution;
    private int intelligence;
    private int wisdom;
    private int charisma;

    DnDCharacter() {
        this.strength = ability(rollDice());
        this.dexterity = ability(rollDice());
        this.constitution = ability(rollDice());
        this.constMod = modifier(this.constitution);
        this.intelligence = ability(rollDice());
        this.wisdom = ability(rollDice());
        this.charisma = ability(rollDice());
    }
    
    int ability(List<Integer> scores) {
        int sum = 0;
        int min = 6;

        for (int score : scores) {
            sum += score;
            if (score < min) {
                min = score;
            }
        }
        return sum - min;
    }

    List<Integer> rollDice() {
        Random random = new Random();
        
        List<Integer> dice = new ArrayList<>();
        for (int i =0; i < 4; i++){
            dice.add(random.nextInt(6) + 1);
        }
        return dice;
    }

    int modifier(int input) {
        return (int) Math.floor((input - 10) / 2.0);        
    }

    int getStrength() { 
        return this.strength; 
    }
    
    int getDexterity() { 
        return this.dexterity; 
    }
    
    int getConstitution() { 
        return this.constitution; 
    }
    
    int getIntelligence() { 
        return this.intelligence; 
    }
    
    int getWisdom() { 
        return wisdom; 
    }
    
    int getCharisma() { 
        return charisma; 
    }

    int getHitpoints() {
        return 10 + constMod;
    }

}

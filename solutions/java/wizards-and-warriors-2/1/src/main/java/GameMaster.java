public class GameMaster {

    public String describe(Character chr){
        return "You're a level " + chr.getLevel() + " " + chr.getCharacterClass() + " with " + chr.getHitPoints() + " hit points.";
    }

     public String describe(Destination dest){
        return "You've arrived at " + dest.getName() + ", which has " + dest.getInhabitants() + " inhabitants.";
    }

    public String describe(TravelMethod tm){
        String end = (tm.equals(TravelMethod.HORSEBACK)) ? "on horseback." : "by walking.";    
        return "You're traveling to your destination " + end;
    }

    public String describe(Character chr, Destination des, TravelMethod tm){
        return describe(chr) + " " + describe(tm) + " " + describe(des);
    }

    public String describe(Character chr, Destination des){
        return describe(chr, des, TravelMethod.WALKING);
    }
}

package Chess;

public class Piece{
    private String color;
    private int[] position;
    public Piece(){
        color = null;
        position = null;
    }

    public String getColor() {
        return color;
    }
    public int[] getPosition() {
        return position;
    }
    public Piece(String color, int[] position) {
        this.color = color;
        this.position = position;

    }
    public void moving_process(int[] whereTo, Piece[][] field, int count, boolean flag) {
        if(flag){
            /*try {
                field[position[0]][position[1]].finalize();
            } catch(Throwable e){
                */field[position[0]][position[1]]=null;/*
            } finally {*/
                setPosition(whereTo);
                field[position[0]][position[1]] = this;
            //}
        }else{
            System.out.println("Invalid move");
            count--;
        }
    }
    public void setPosition(int[] position) {
        this.position = position;
    }
}

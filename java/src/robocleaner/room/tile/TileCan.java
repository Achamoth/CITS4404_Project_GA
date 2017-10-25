package robocleaner.room.tile;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class TileCan implements ITile {
    public static TileCan instance = new TileCan();

    private TileCan() {
    }

    @Override
    public char getSymbol() {
        return 'C';
    }

    @Override
    public ITile getInstance() {
        return instance;
    }

    @Override
    public boolean isCollectable() {
        return true;
    }

    @Override
    public int getPoints() {
        return 10;
    }
}

package robocleaner.room.tile;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class TileEmpty implements ITile {
    public static TileEmpty instance = new TileEmpty();

    private TileEmpty() {
    }

    @Override
    public char getSymbol() {
        return '.';
    }

    @Override
    public ITile getInstance() {
        return instance;
    }
}

package robocleaner.room.tile;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class TileWall implements ITile {
    public static TileWall instance = new TileWall();

    private TileWall() {
    }

    @Override
    public char getSymbol() {
        return 'W';
    }

    @Override
    public ITile getInstance() {
        return instance;
    }

    @Override
    public boolean isSolid() {
        return true;
    }
}

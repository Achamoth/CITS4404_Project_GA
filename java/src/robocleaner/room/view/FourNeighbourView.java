package robocleaner.room.view;

import robocleaner.room.IRoom;
import robocleaner.room.tile.ITile;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class FourNeighbourView implements IView {
    @Override
    public int getSize() {
        return 5;
    }

    @Override
    public ITile[] getTiles(IRoom rm, int row, int col) {
        return new ITile[]{
                rm.get(row, col),
                rm.get(row, col - 1),
                rm.get(row, col + 1),
                rm.get(row - 1, col),
                rm.get(row + 1, col)
        };
    }
}

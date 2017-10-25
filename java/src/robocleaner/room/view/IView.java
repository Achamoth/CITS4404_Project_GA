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
public interface IView {
    int getSize();

    ITile[] getTiles(IRoom rm, int row, int col);
}

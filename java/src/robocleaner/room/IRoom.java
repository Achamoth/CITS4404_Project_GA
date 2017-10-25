package robocleaner.room;

import robocleaner.room.tile.ITile;

import java.util.Set;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public interface IRoom {
    ITile get(int r, int c);

    ITile set(int r, int c, ITile cell);

    int getRows();

    int getColumns();

    Set<ITile> getTileSet();

    int getTileIndex(ITile tile);
}

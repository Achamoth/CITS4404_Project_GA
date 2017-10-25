package robocleaner.room;

import robocleaner.room.tile.ITile;

import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.function.BiFunction;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class Room implements IRoom {

    protected final int rows, cols;
    protected final ITile[][] content;
    protected final ITile outOfBounds;

    protected final Set<ITile> tileSet = new TreeSet<>();
    protected final Map<ITile, Integer> tileMap = new TreeMap<>();

    public Room(int rows, int cols, Set<ITile> tileSet, ITile outOfBounds) {
        content = new ITile[rows][cols];
        this.rows = rows;
        this.cols = cols;
        this.outOfBounds = outOfBounds;

        this.tileSet.clear();
        this.tileSet.addAll(tileSet);
        this.tileMap.clear();
        int i = 0;
        for (ITile tile : getTileSet()) {
            this.tileMap.put(tile, 0);
            i++;
        }
    }

    public static Room make(int rows, int cols, Set<ITile> tileSet, ITile outOfBounds, BiFunction<Integer, Integer, ITile> filler) {
        Room rm = new Room(rows, cols, tileSet, outOfBounds);
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                rm.content[r][c] = filler.apply(r, c);
            }
        }
        return rm;
    }

    public static Room make(int rows, int cols, Set<ITile> tileSet, ITile outOfBounds, ITile[][] content) {
        return make(rows, cols, tileSet, outOfBounds, (r, c) -> content[r][c]);
    }

    public ITile get(int r, int c) {
        if (r < 0 || c < 0 || r >= rows || c >= cols)
            return outOfBounds;
        return content[r][c];
    }

    public ITile set(int r, int c, ITile cell) {
        ITile prev = content[r][c];
        content[r][c] = cell;
        return prev;
    }

    @Override
    public int getRows() {
        return rows;
    }

    @Override
    public int getColumns() {
        return cols;
    }

    @Override
    public String toString() {
        StringBuilder build = new StringBuilder();
        for (int r = -1; r <= rows; r++) {
            for (int c = -1; c <= cols; c++) {
                build.append(get(r, c).getSymbol());
            }
            if (r != rows)
                build.append('\n');
        }
        return build.toString();
    }


    @Override
    public Set<ITile> getTileSet() {
        return new TreeSet<>(tileSet);
    }

    @Override
    public int getTileIndex(ITile tile) {
        return 0;
    }

}

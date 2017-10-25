package robocleaner.room.tile;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public interface ITile extends Comparable<ITile> {
    char getSymbol();

    ITile getInstance();

    default boolean isSolid(){ return false; }

    default boolean isCollectable(){ return false; }

    default int getPoints(){ return 0; }

    @Override
    default int compareTo(ITile o) {
        return Character.compare(this.getSymbol(), o.getSymbol());
    }
}

package robocleaner.robot.action;

import robocleaner.robot.IRobot;
import robocleaner.room.IRoom;

import java.util.Random;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public interface IAction extends Comparable<IAction> {
    char getSymbol();

    void perform(Random rand, IRoom rm, IRobot robot);

    IAction getInstance();

    @Override
    default int compareTo(IAction o) {
        return Character.compare(this.getSymbol(), o.getSymbol());
    }
}

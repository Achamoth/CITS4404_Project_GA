package robocleaner.robot.action;

import robocleaner.robot.IRobot;
import robocleaner.room.IRoom;

import java.util.Random;

/**
 * Created 26/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class ActionNothing extends AbstractAction {
    public static final ActionNothing instance = new ActionNothing();

    private ActionNothing() {
    }

    @Override
    public char getSymbol() {
        return ' ';
    }

    @Override
    public void perform(Random rand, IRoom rm, IRobot robot) {
        //Nothing
    }

    @Override
    public IAction getInstance() {
        return instance;
    }
}

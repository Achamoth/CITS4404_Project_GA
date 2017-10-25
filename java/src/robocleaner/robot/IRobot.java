package robocleaner.robot;

import robocleaner.robot.action.IAction;
import robocleaner.room.IRoom;
import robocleaner.room.view.IView;

import java.util.Set;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public interface IRobot {

    IRoom getRoom();

    Set<IAction> getActionSet();

    int getActionIndex(IAction action);

    int getRow();

    void setRow(int r);

    int getCol();

    void setCol(int c);

    IView getView();

    IAction getAction();

    void resetPoints();

    int getPoints();

    void addPoints(int points);
}

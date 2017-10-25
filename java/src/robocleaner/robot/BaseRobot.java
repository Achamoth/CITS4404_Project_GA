package robocleaner.robot;

import robocleaner.robot.action.IAction;
import robocleaner.room.IRoom;
import robocleaner.room.view.IView;

import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public abstract class BaseRobot implements IRobot {
    private final Set<IAction> actionSet;
    private final Map<IAction, Integer> actionMap;
    private final IRoom room;
    private final IView view;
    private int row, col;
    private int points;


    public BaseRobot(Set<IAction> actionSet, IRoom room, IView view, int x, int y) {
        this.actionSet = new TreeSet<>();
        this.actionSet.addAll(actionSet);
        this.actionMap = new TreeMap<>();
        int i = 0;
        for (IAction action : getActionSet()) {
            this.actionMap.put(action, i);
            i++;
        }
        this.room = room;
        this.view = view;
        this.row = x;
        this.col = y;
        this.points = 0;
    }

    @Override
    public IRoom getRoom() {
        return room;
    }

    @Override
    public Set<IAction> getActionSet() {
        return new TreeSet<>(actionSet);
    }

    @Override
    public int getActionIndex(IAction action) {
        return this.actionMap.get(action);
    }

    @Override
    public int getRow() {
        return row;
    }

    @Override
    public void setRow(int row) {
        this.row = row;
    }

    @Override
    public int getCol() {
        return col;
    }

    @Override
    public void setCol(int col) {
        this.col = col;
    }

    @Override
    public IView getView() {
        return view;
    }

    @Override
    public abstract IAction getAction();

    @Override
    public void resetPoints() {
        this.points = 0;
    }

    @Override
    public int getPoints() {
        return this.points;
    }

    @Override
    public void addPoints(int points) {
        this.points += points;
    }
}

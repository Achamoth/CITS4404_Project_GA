package robocleaner;

import org.jenetics.*;
import org.jenetics.engine.Engine;
import org.jenetics.engine.EvolutionResult;
import org.jenetics.util.Factory;
import robocleaner.robot.ActionChromosome;
import robocleaner.robot.GeneRobot;
import robocleaner.robot.action.*;
import robocleaner.room.IRoom;
import robocleaner.room.Room;
import robocleaner.room.tile.ITile;
import robocleaner.room.tile.TileCan;
import robocleaner.room.tile.TileEmpty;
import robocleaner.room.tile.TileWall;
import robocleaner.room.view.FourNeighbourView;
import robocleaner.room.view.IView;

import java.util.Arrays;
import java.util.Random;
import java.util.Set;
import java.util.TreeSet;
import java.util.stream.Collectors;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class Simulation {
    public static final Random rand = new Random(0);

    static Set<ITile> tileSet = Arrays.stream(new ITile[]{TileEmpty.instance, TileCan.instance, TileWall.instance})
            .collect(Collectors.toSet());
    static Set<IAction> actionSet = new TreeSet<IAction>(Arrays.stream(new IAction[]{
            ActionUp.instance, ActionDown.instance, ActionLeft.instance, ActionRight.instance,
            ActionPickUp.instance, ActionRandom.instance
    }).collect(Collectors.toSet()));
    static IAction[] actions = actionSet.toArray(new IAction[0]);

    static IView view = new FourNeighbourView();

    public Simulation(){}

    // 2.) Definition of the fitness function.
    private static int eval(Genotype<IActionGene> gt) {
        Room rm = Room.make(10, 10, tileSet, TileWall.instance, (r, c) ->
                rand.nextDouble() < 0.5 ? TileCan.instance : TileEmpty.instance
        );
        ActionChromosome chroma = gt.getChromosome()
                .as(ActionChromosome.class);
        //Create robot
        GeneRobot robot = new GeneRobot(actionSet, rm, view, rand.nextInt(rm.getRows()), rand.nextInt(rm.getColumns()));
        robot.loadGene(chroma.getActionArray());
        for(int i = 0; i < 200; i++)
            robot.getAction().perform(rand, rm, robot);
        return robot.getPoints();
    }

    private static boolean validator(Genotype<IActionGene> gt) {
        return true;
    }

    public static void main(String[] args) {
        IRoom baseRoom = Room.make(10, 10, tileSet, TileWall.instance, (r, c) ->
                rand.nextDouble() < 0.5 ? TileCan.instance : TileEmpty.instance
        );
        GeneRobot baseRobot = new GeneRobot(actionSet, baseRoom, view, rand.nextInt(baseRoom.getRows()), rand.nextInt(baseRoom.getColumns()));
        int geneLength = baseRobot.gene.length;
        //System.out.println(rm.toString());
        System.out.println("Gene Length: " + geneLength);


        // 1.) Define the genotype (factory) suitable
        //     for the problem.
        Factory<Genotype<IActionGene>> gtf =
                Genotype.of(new ActionChromosome(actions, geneLength));

        // 3.) Create the execution environment.
        Engine<IActionGene, Integer> engine = Engine
                .builder(Simulation::eval, gtf)
                .maximizing()
                .optimize(Optimize.MAXIMUM)
                .selector(new TournamentSelector<>(3))
                .alterers(
                        new UniformCrossover<>(0.5),
                        new Mutator<>(0.15)
                )
                .survivorsFraction(0.1)
                .genotypeValidator(Simulation::validator)
                .populationSize(500)
                .build();

        // 4.) Start the execution (evolution) and
        //     collect the result.
        Genotype<IActionGene> result = engine.stream()
                .limit(100)
                .collect(EvolutionResult.toBestGenotype());

        System.out.println(result);
        System.out.println("Score: " + eval(result));
    }
}

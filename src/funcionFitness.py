'''
Created on Apr 26, 2016

@author: carlosandressierra
'''

class FuncionFitness(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def calcularFitness(self):
        return 10
        
        
 '''
 import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;


public class FitnessFunction 
{
    //Time table
    private int[][] times_table = null; 
    
    private int j, m;
    
    private int[][] tasks = null;
    
    /**
     * Constructor with data set path
     * @param file
     */
    public FitnessFunction(int machines, int jobs, String file)
    {
        this.times_table = new int[jobs][machines];
        
        this.m = machines;
        this.j = jobs;
        
        BufferedReader brBackground;
        String[] lineBackground;
        String line = "";
        
        try 
        {
            brBackground = new BufferedReader(new FileReader( file ));
            line = brBackground.readLine();
            
            int row = 0;    //Initial row of times times
            
            while(line != null) 
            {
                lineBackground = line.split(" ");
                
                for(int i = 0; i < machines; i++)
                {
                    times_table[row][i] = Integer.parseInt( lineBackground[i] );
                }
                    
                row++;
                line = brBackground.readLine();
            }
        } 
        catch (FileNotFoundException e) 
        {
            e.printStackTrace();
        } 
        catch (IOException e) 
        {
            e.printStackTrace();
        }
    }
    
    
    /**
     * 
     * @param individual
     */
    public void start(int[] individual) 
    {
        this.tasks = new int[j * m][2];
        int machine, job;
        
        for(int i = 0; i < individual.length; i++)
        {
            job = (individual[i] - 1) / j;
            machine = (individual[i] - 1) % m;
            
            tasks[i][0] = job;
            tasks[i][1] = machine;
        } 
    }

    
    
    /**
     * This method return fitness of a permutation with sequence of machines per job
     * @param individual
     * @return fitness of individual
     */
    public int calculateFitness_orderMachines(int[] individual)
    {
        this.start(individual);
        
        int[] time_finish = null;
        int[] machines = null;
        boolean[] jobs = null;
        
        time_finish = new int[m];
        
        machines = new int[m];
        jobs = new boolean[j];
        
        
        for(int i = 0; i < machines.length; i++)
        {
            machines[i] = -1;
            jobs[i] = false;
        }
        
        
        int tasks_finished = 0;
        int time = 0;
        
        while(tasks_finished < (m * j))
        {
            for(int i = 0; i < machines.length; i++)
            {
                int[] passed = new int[j];
                
                if(machines[i] == -1)
                {
                    for(int k = 0; k < this.tasks.length; k++)
                    {
                        if(this.tasks[k][1] == i)
                        {
                            if( !jobs[ this.tasks[k][0] ] && passed[this.tasks[k][0]] != -1)
                            {
                                machines[i] = this.tasks[k][0];
                                jobs[ this.tasks[k][0] ] = true;
                                time_finish[i] = time + this.times_table[ this.tasks[k][0] ][ i ];
                                this.tasks[k][0] = this.tasks[k][1] = -2;
                                
                                break;
                            }
                        }
                        
                        if(this.tasks[k][0] >= 0)
                            passed[this.tasks[k][0]] = -1;
                    }
                }
                else
                {
                    if(time_finish[i] == time)
                    {
                        jobs[ machines[i] ] = false;
                        machines[i] = -1;
                        tasks_finished++;
                        i--;
                    }
                }
            }
            
            time++;
        }
        
        return (time - 1);
    }
    
    
    /**
     * 
     * @param individual
     */
    public void start_jobs(int[] individual) 
    {
        this.tasks = new int[j * m][2];
        int machine, job;
        
        for(int i = 0; i < individual.length; i++)
        {
            machine = (individual[i] - 1) / m;
            job = (individual[i] - 1) % j;
            
            tasks[i][0] = job;
            tasks[i][1] = machine;
        } 
    }
    
    
    /**
     * This method return fitness of a permutation with sequence of jobs per machine
     * @param individual
     * @return fitness of individual
     */
    public int calculateFitness_orderJobs(int[] individual)
    {
        this.start_jobs(individual);
        
        int[] time_finish = null;
        int[] jobs = null;
        boolean[] machines = null;
        
        time_finish = new int[m];
        
        machines = new boolean[m];
        jobs = new int[j];
        
        
        for(int i = 0; i < machines.length; i++)
        {
            machines[i] = false;    
            jobs[i] = -1;
        }
        
        
        int tasks_finished = 0;
        int time = 0;
        
        while(tasks_finished < (m * j))
        {
            for(int i = 0; i < jobs.length; i++)
            {
                int[] passed = new int[j];
                
                if(jobs[i] == -1)
                {
                    for(int k = 0; k < this.tasks.length; k++)
                    {
                        if(this.tasks[k][1] == i)
                        {
                            if( !machines[ this.tasks[k][0] ] && passed[this.tasks[k][0]] != -1)
                            {
                                jobs[i] = this.tasks[k][0];
                                machines[ this.tasks[k][0] ] = true;
                                time_finish[i] = time + this.times_table[ this.tasks[k][1] ][ this.tasks[k][0] ];
                                this.tasks[k][0] = this.tasks[k][1] = -2;
                                
                                break;
                            }
                        }
                        
                        if(this.tasks[k][0] >= 0)
                            passed[this.tasks[k][0]] = -1;
                    }
                }
                else
                {
                    if(time_finish[i] == time)
                    {
                        machines[ jobs[i] ] = false;
                        jobs[i] = -1;
                        tasks_finished++;
                        i--;
                    }
                }
            }
            
            time++;
        }
        
        return (time - 1);
    }
    
    
    
    /**
     * This method return fitness of a permutation with sequence of jobs per machine
     * @param individual
     * @return fitness of individual
     */
    public int calculateFitness_identicalMachine(int[] individual)
    {
        this.start(individual);
        
        int[] time_finish = null;
        int[] machines = null;
        boolean[] jobs = null;
        
        time_finish = new int[m];
        
        machines = new int[m];
        jobs = new boolean[j];
        
        
        for(int i = 0; i < machines.length; i++)
        {
            machines[i] = -1;
            jobs[i] = false;
        }
        
        
        int tasks_finished = 0;
        int time = 0;
        
        while(tasks_finished < (m * j))
        {
            for(int i = 0; i < machines.length; i++)
            {
                int[] passed = new int[j];
                
                if(machines[i] == -1)
                {
                    for(int k = 0; k < this.tasks.length; k++)
                    {
                        if(this.tasks[k][1] == i)
                        {
                            if( !jobs[ this.tasks[k][0] ] && passed[this.tasks[k][0]] != -1)
                            {
                                machines[i] = this.tasks[k][0];
                                jobs[ this.tasks[k][0] ] = true;
                                time_finish[i] = time + this.times_table[ this.tasks[k][0] ][ i ];
                                this.tasks[k][0] = this.tasks[k][1] = -2;
                                
                                break;
                            }
                        }
                        
                        if(this.tasks[k][0] >= 0)
                            passed[this.tasks[k][0]] = -1;
                    }
                }
                else
                {
                    if(time_finish[i] == time)
                    {
                        jobs[ machines[i] ] = false;
                        machines[i] = -1;
                        tasks_finished++;
                        i--;
                    }
                }
            }
            
            time++;
        }
        
        return (time - 1);
    }
    
    
    public void printTable()
    {
        for(int i = 0; i < this.times_table.length; i++)
        {
            for(int j = 0; j < this.times_table.length; j++)
            {
                System.out.print(times_table[i][j] + "\t");
            }
            ystem.out.println();
        }
    }
    
    
    public static void main(String args[])
    {
        int machines = Integer.parseInt( args[0] );
        String file = args[1];
        
        FitnessFunction fitness = new FitnessFunction(machines, machines, file);
        
        int[] individual = {6, 2, 20, 14, 13, 16, 12, 9, 10, 8, 1, 24, 25, 23, 22, 5, 11, 7, 19, 18, 4, 21, 17, 15, 3};
        
        System.out.println(fitness.calculateFitness_orderJobs(individual));
    }
    
}
            '''     
      
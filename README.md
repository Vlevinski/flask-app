# Flask MySQL Docker
# MySQL Docker
    ( unsecure version , crypto tests)

## Docker image
The latest from docker hub

## Running

    '''
    docker-compose up
       or
    docker-compose down
    '''
## Test

   '''
   mysql -h 0.0.0.0 -u root -p -e "SELECT version()"
       or
   ./test.test.sh
   '''

## Python test

    '''
    python ./app/app.py
    '''
## DB by default:

    '''
    ./db/user.sql
    '''

## Manual access:
    '''
    mysql> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              /
    /  notes              |
    | performance_schema |
    | sys                |
    +--------------------+
    4 rows in set (0.01 sec)
    
    mysql> slect * from user;
    (1,'Nick Parson','nick@gmail.com',12345678,'None'),
    (2,'Ralph Pen','ralph@gmail.com',12398765,'Remote'),
    (3,'Hellen Duck','hellenl@gmail.com',12356789,'Next door');
    
    mysql> select version();
    +-----------+
    | version() |
    +-----------+
    | 8.0.27    |
    +-----------+
    1 row in set (0.00 sec)
    
    mysql> 
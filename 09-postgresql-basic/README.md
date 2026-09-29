# 09 --- PostgreSQL Basic Example

This example demonstrates **PostgreSQL as a standalone database
system**.

The purpose of this example is to introduce:

-   starting PostgreSQL with Docker Compose;
-   connecting to PostgreSQL with `psql`;
-   creating a database schema from a SQL file;
-   running sample SQL queries;
-   moving correctly between the operating-system terminal and the
    PostgreSQL prompt;
-   inspecting and stopping the Docker database service.

This example is intentionally **not tied to Flask, FastAPI, Django,
Node.js, or another web framework**. The focus is PostgreSQL itself.

------------------------------------------------------------------------

## 1. Basic Architecture

The environment can be viewed as:

``` text
macOS / Linux Terminal
        |
        | docker compose ...
        v
Docker Compose
        |
        v
PostgreSQL Container
        |
        | psql
        v
PostgreSQL Database
        |
        +--> schema.sql
        |
        +--> sample_queries.sql
```

The important distinction is that **Docker commands and SQL/psql
commands are not entered at the same prompt**.

------------------------------------------------------------------------

## 2. Command Environments

During this example, you will work in two main environments.

### Environment A --- Normal terminal

A normal terminal prompt may look similar to:

``` text
$
```

or:

``` text
%
```

Run commands such as:

``` bash
docker compose up -d
docker compose ps
docker compose logs db
docker compose down
```

from the normal terminal.

### Environment B --- PostgreSQL `psql`

After connecting to PostgreSQL, the prompt may look similar to:

``` text
framework_demo=#
```

Run PostgreSQL commands such as:

``` sql
\i /sql/schema.sql
\i /sql/sample_queries.sql
\dt
\q
```

at the `psql` prompt.

### Transition

``` text
Normal Terminal
      |
      | docker compose exec db psql ...
      v
PostgreSQL psql Prompt
      |
      | \q
      v
Normal Terminal
```

This transition is important when following the instructions below.

------------------------------------------------------------------------

## 3. Prerequisites

This example uses Docker Compose.

Verify Docker:

``` bash
docker --version
```

Verify Docker Compose:

``` bash
docker compose version
```

Docker Desktop should be running before starting the database.

------------------------------------------------------------------------

## 4. Project Files

The project should contain a Docker Compose configuration and the SQL
files used by PostgreSQL.

A simplified structure may look like:

``` text
09-postgresql-basic/
├── docker-compose.yml
├── README.md
└── sql/
    ├── schema.sql
    └── sample_queries.sql
```

The Docker Compose file determines how the local `sql/` directory is
made available inside the PostgreSQL container.

The existing commands in this example expect the SQL files to be
accessible inside the container as:

``` text
/sql/schema.sql
/sql/sample_queries.sql
```

------------------------------------------------------------------------

# Part A --- Start PostgreSQL

## 5. Go to the PostgreSQL Example Directory

**Run this in the normal terminal.**

Navigate to the directory containing:

``` text
docker-compose.yml
```

For example:

``` bash
cd 09-postgresql-basic
```

Verify the files:

``` bash
pwd
ls
```

You should be able to see the Docker Compose file.

------------------------------------------------------------------------

## 6. Validate the Docker Compose Configuration

**Normal terminal:**

``` bash
docker compose config
```

This asks Docker Compose to parse and display the resolved
configuration.

It is useful for detecting YAML or Compose configuration problems before
starting the service.

------------------------------------------------------------------------

## 7. Start PostgreSQL

**Normal terminal:**

``` bash
docker compose up -d
```

The `-d` option means **detached mode**.

The PostgreSQL container runs in the background and the terminal prompt
returns to you.

Conceptually:

``` text
docker compose up -d
        |
        v
Docker reads docker-compose.yml
        |
        v
PostgreSQL container starts
        |
        v
Database service runs in background
```

------------------------------------------------------------------------

## 8. Check the Container

**Normal terminal:**

``` bash
docker compose ps
```

Use this command to verify that the database service is running.

If the service is not running correctly, inspect its logs.

------------------------------------------------------------------------

## 9. View PostgreSQL Logs

**Normal terminal:**

``` bash
docker compose logs db
```

The name:

``` text
db
```

refers to the database service defined in the Docker Compose
configuration.

Logs are useful for diagnosing:

-   startup failures;
-   configuration problems;
-   database initialization errors;
-   port conflicts.

------------------------------------------------------------------------

# Part B --- Connect to PostgreSQL

## 10. Open `psql`

**Run this command from the normal terminal:**

``` bash
docker compose exec db psql -U classroom -d framework_demo
```

The command means:

``` text
docker compose exec
        |
        +--> execute a command in a running service

db
        |
        +--> use the Docker Compose service named db

psql
        |
        +--> start the PostgreSQL command-line client

-U classroom
        |
        +--> connect as PostgreSQL user classroom

-d framework_demo
        |
        +--> connect to database framework_demo
```

After the connection succeeds, your prompt should change.

For example:

``` text
framework_demo=#
```

You are now **inside `psql`**.

Do not enter `docker compose` commands at this prompt.

------------------------------------------------------------------------

# Part C --- Load the SQL Files

## 11. Run the Schema File

**Inside `psql`:**

``` sql
\i /sql/schema.sql
```

The `\i` command tells `psql` to read and execute commands from a file.

Conceptually:

``` text
psql
  |
  | \i /sql/schema.sql
  v
schema.sql
  |
  v
CREATE TABLE / schema commands
  |
  v
PostgreSQL database
```

------------------------------------------------------------------------

## 12. Verify the Tables

**Inside `psql`:**

``` sql
\dt
```

This lists tables visible in the current database/schema.

This is a useful checkpoint after running:

``` sql
\i /sql/schema.sql
```

If the expected tables appear, the schema loaded successfully.

------------------------------------------------------------------------

## 13. Run the Sample Queries

**Inside `psql`:**

``` sql
\i /sql/sample_queries.sql
```

This executes the SQL statements stored in the sample query file.

The flow is:

``` text
sample_queries.sql
        |
        v
      psql
        |
        v
PostgreSQL executes SQL
        |
        v
Results displayed in terminal
```

------------------------------------------------------------------------

## 14. Useful `psql` Commands

These commands are entered **inside `psql`**.

List tables:

``` sql
\dt
```

Describe a table:

``` sql
\d table_name
```

Show connection information:

``` sql
\conninfo
```

List databases:

``` sql
\l
```

Show help for `psql` commands:

``` sql
\?
```

Exit PostgreSQL:

``` sql
\q
```

------------------------------------------------------------------------

## 15. If Query Output Shows `(END)`

Long query results may open in a terminal pager.

You may see:

``` text
(END)
```

Press:

``` text
q
```

to exit the pager and return to the PostgreSQL prompt.

Important:

``` text
q
```

exits the **pager**.

``` sql
\q
```

exits **psql**.

These are different commands.

------------------------------------------------------------------------

# Part D --- Return to the Normal Terminal

## 16. Exit `psql`

**Inside `psql`:**

``` sql
\q
```

After running `\q`, you return to the normal macOS/Linux terminal.

The transition is:

``` text
framework_demo=#
        |
        | \q
        v
Normal terminal prompt
```

Docker commands can now be entered again.

------------------------------------------------------------------------

# Part E --- Stop PostgreSQL

## 17. Stop the Docker Services

**Normal terminal:**

``` bash
docker compose down
```

This stops and removes the Compose containers and network.

For normal classroom use, this is the recommended stop command.

------------------------------------------------------------------------

## 18. Important: Do Not Add `-v` Unless You Intend to Delete the Database Volume

The command:

``` bash
docker compose down
```

is different from:

``` bash
docker compose down -v
```

The `-v` option also removes named volumes associated with the Compose
project.

For a PostgreSQL database, that may remove the stored database data.

Therefore:

``` bash
docker compose down
```

should be the normal command.

Use:

``` bash
docker compose down -v
```

only when you **intentionally want to remove the named database volume
and reset the database environment**.

------------------------------------------------------------------------

# Part F --- Docker Compose Diagnostics

## 19. Inspect the Compose Configuration

**Normal terminal:**

``` bash
docker compose config
```

Use this to inspect the resolved Docker Compose configuration.

------------------------------------------------------------------------

## 20. Check Service Status

**Normal terminal:**

``` bash
docker compose ps
```

This shows the current status of the services.

------------------------------------------------------------------------

## 21. Check Database Logs

**Normal terminal:**

``` bash
docker compose logs db
```

For continuously updating logs, you can use:

``` bash
docker compose logs -f db
```

Press:

``` text
Ctrl+C
```

to stop following the logs.

------------------------------------------------------------------------

## 22. Inspect a `version` Entry in the Compose File

The original example includes:

``` bash
grep -n "version" docker-compose.yml
```

This searches `docker-compose.yml` for a line containing the word
`version`.

This can be useful when investigating Docker Compose warnings related to
an older Compose-file `version` field.

------------------------------------------------------------------------

## 23. Run Compose in the Foreground

The original example also includes:

``` bash
docker compose -f ./docker-compose.yml up
```

Unlike:

``` bash
docker compose up -d
```

this runs the services in the foreground so the container logs remain
visible in the terminal.

Use:

``` text
Ctrl+C
```

to stop foreground execution.

For routine classroom work, detached mode is usually easier:

``` bash
docker compose up -d
```

------------------------------------------------------------------------

# Part G --- Troubleshooting

## 24. `docker compose` Cannot Find the Configuration File

If Docker reports that it cannot find a Compose file, check your current
directory:

``` bash
pwd
ls
```

Make sure you are in the directory containing:

``` text
docker-compose.yml
```

Then retry:

``` bash
docker compose up -d
```

------------------------------------------------------------------------

## 25. The `db` Service Is Not Running

Check:

``` bash
docker compose ps
```

Then inspect:

``` bash
docker compose logs db
```

If the container failed during startup, the logs usually provide the
most useful error information.

------------------------------------------------------------------------

## 26. `psql` Connection Fails

First confirm the database service is running:

``` bash
docker compose ps
```

Then retry:

``` bash
docker compose exec db psql -U classroom -d framework_demo
```

Make sure the Docker Compose configuration actually defines:

-   a service named `db`;
-   the `classroom` PostgreSQL user;
-   the `framework_demo` database.

------------------------------------------------------------------------

## 27. `/sql/schema.sql` Cannot Be Found

If this command:

``` sql
\i /sql/schema.sql
```

reports that the file does not exist, first exit `psql`:

``` sql
\q
```

You are now back at the normal terminal.

Check the project:

``` bash
ls
ls sql
```

The local project should contain the expected SQL files.

Then inspect the Compose configuration:

``` bash
docker compose config
```

The Docker configuration must make those files available inside the
container at the path expected by the README:

``` text
/sql/
```

------------------------------------------------------------------------

## 28. `\dt` Says No Relations Were Found

If:

``` sql
\dt
```

reports no relations, verify that the schema file executed successfully:

``` sql
\i /sql/schema.sql
```

Then run:

``` sql
\dt
```

again.

Also confirm that you connected to the intended database:

``` sql
\conninfo
```

The expected database for this example is:

``` text
framework_demo
```

------------------------------------------------------------------------

## 29. Docker Reports a Port Conflict

If PostgreSQL cannot start because its host port is already in use,
inspect the running containers:

``` bash
docker ps
```

Also inspect the Compose configuration:

``` bash
docker compose config
```

Another local PostgreSQL instance or Docker container may already be
using the configured host port.

------------------------------------------------------------------------

# Part H --- Complete Recommended Workflow

## 30. Terminal → PostgreSQL → Terminal

The complete workflow is:

### Step 1 --- Normal terminal

``` bash
docker compose config
docker compose up -d
docker compose ps
```

### Step 2 --- Normal terminal: enter PostgreSQL

``` bash
docker compose exec db psql -U classroom -d framework_demo
```

### Step 3 --- Inside `psql`

``` sql
\i /sql/schema.sql
\dt
\i /sql/sample_queries.sql
```

### Step 4 --- Inside `psql`: exit

``` sql
\q
```

### Step 5 --- Back in the normal terminal

``` bash
docker compose down
```

The environment transition is:

``` text
Normal Terminal
      |
      | docker compose up -d
      |
      | docker compose exec db psql ...
      v
PostgreSQL psql
      |
      | \i /sql/schema.sql
      | \dt
      | \i /sql/sample_queries.sql
      | \q
      v
Normal Terminal
      |
      | docker compose down
      v
Finished
```

------------------------------------------------------------------------

## 31. Quick Command Reference

  --------------------------------------------------------------------------------------------------------------
  Environment             Goal                    Command
  ----------------------- ----------------------- --------------------------------------------------------------
  Terminal                Validate Compose        `docker compose config`

  Terminal                Start PostgreSQL        `docker compose up -d`

  Terminal                Check services          `docker compose ps`

  Terminal                View DB logs            `docker compose logs db`

  Terminal                Enter PostgreSQL        `docker compose exec db psql -U classroom -d framework_demo`

  `psql`                  Load schema             `\i /sql/schema.sql`

  `psql`                  List tables             `\dt`

  `psql`                  Show connection         `\conninfo`

  `psql`                  Run sample queries      `\i /sql/sample_queries.sql`

  Pager                   Exit `(END)` screen     `q`

  `psql`                  Exit PostgreSQL         `\q`

  Terminal                Stop services           `docker compose down`
  --------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Learning Outcomes

After completing this example, students should be able to:

1.  Explain the role of PostgreSQL as a database system independent of a
    web framework.
2.  Start PostgreSQL using Docker Compose.
3.  Distinguish a normal operating-system terminal from the PostgreSQL
    `psql` prompt.
4.  Connect to a PostgreSQL database running in Docker.
5.  Explain the meaning of the `-U` and `-d` options in the `psql`
    command.
6.  Execute a SQL file with the `\i` command.
7.  Verify database tables with `\dt`.
8.  Run sample SQL queries from a file.
9.  Exit the terminal pager with `q`.
10. Exit PostgreSQL with `\q`.
11. Inspect Docker Compose services and PostgreSQL logs.
12. Explain the difference between `docker compose down` and
    `docker compose down -v`.
13. Trace the workflow from the local terminal to Docker, PostgreSQL,
    and back to the terminal.

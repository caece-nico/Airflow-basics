# Notas importantes de la implementacion de Airflow.

1. [Porque no veo mi DAG](#1.-porque-no-veo-mi-dag?)

## 1. Porque no veo mi DAG?

````
The little secret of the Web server and the Scheduler
When I used Airflow for the first time I was really happy!

My DAG was ready (beautiful code), I put it into the folder DAGs, Airflow was running, I check the Web server and the Scheduler, everything was running perfectly, I refreshed the page to see my DAG and...

NOTHING!

No sign of my DAG.

The worst part is that I can predict it will happen to you too.

So why is that? Is there a way to fix this?



Well, in the previous video, you learned that both the webserver and scheduler parse your DAGs. You can configure this parsing process with different configuration settings.

With the Scheduler:

min_file_process_interval

Number of seconds after which a DAG file is parsed. The DAG file is parsed every min_file_process_interval number of seconds. Updates to DAGs are reflected after this interval.

dag_dir_list_interval

How often (in seconds) to scan the DAGs directory for new files. Default to 5 minutes.

Those 2 settings tell you that you have to wait up 5 minutes before your DAG gets detected by the scheduler and then it is parsed every 30 seconds by default.



With the Webserver:

worker_refresh_interval

Number of seconds to wait before refreshing a batch of workers. 30 seconds by default.

This setting tells you that every 30 seconds, the web server parses for new DAG in your DAG folder.



So, back to my issue, I had to wait 5 minutes before getting my DAG ready to be triggered and then I was relieved 😀

Remember

By default, when you add a new DAG you will have to wait up to 5 minutes before getting your DAG on the UI and then if you modify it, you will have to wait up to 30 seconds before getting your DAG updated.

You will never be surprised again 😎
```
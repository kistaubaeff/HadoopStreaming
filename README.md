# Module2 Hadoop Streaming

echo "abc def abc de df def xyz" | python mapper.py
echo "abc def abc de df def xyz" | python mapper.py | sort | python reducer.py


hdfs dfs -put in in

hdfs dfs -rm -r out

yarn jar /opt/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py  -input in -output out

## Linting

```bash
pylint *.py
```

## Testing

```bash
cat test.in.txt | python mapper.py | sort | python reducer.py | diff -w test.out.txt -
```

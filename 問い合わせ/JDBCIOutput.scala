import org.apache.flink.api.java.io.jdbc.JDBCOutputFormat
import org.apache.flink.api.scala.DataSet
import org.apache.flink.types.Row

val inputPath: String = "/root/student.txt"

val outputJDBC: JDBCOutputFormat = JDBCOutputFormat.buildJDBCOutputFormat().
  setDrivername("org.postgresql.Driver").
  setDBUrl("jdbc:postgresql://localhost:5432/test").
  setUsername("postgres").
  setPassword("Psqlpwd01!").
  setQuery("INSERT INTO student VALUES(?, ?, ?)").
  finish()

val records: DataSet[Row] = for (line <- benv.readTextFile(inputPath)) yield {
  line.split(',') match {
    case Array(id, name, money) =>
      val row: Row = new Row(3)
      row.setField(0, id)
      row.setField(1, name)
      row.setField(2, BigDecimal(money))
      row
  }
}

records.output(outputJDBC)

benv.execute()

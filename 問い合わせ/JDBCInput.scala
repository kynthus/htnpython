import org.apache.flink.api.common.typeinfo.Types
import org.apache.flink.api.java.io.jdbc.JDBCInputFormat
import org.apache.flink.api.java.typeutils.RowTypeInfo

val inputJDBC: JDBCInputFormat = JDBCInputFormat.buildJDBCInputFormat().
  setDrivername("org.postgresql.Driver").
  setDBUrl("jdbc:postgresql://localhost:5432/test").
  setUsername("postgres").
  setPassword("Psqlpwd01!").
  setRowTypeInfo {
    new RowTypeInfo(
      Types.STRING,
      Types.STRING,
      Types.BIG_DEC
    )
  }.
  setQuery("SELECT * FROM student").
  finish()

val outputPath: String = "/root/student.txt"

val updated: DataSet[Row] = for (record <- benv.createInput(inputJDBC)) yield {
  record.setField(2, 54321)
  record
}

updated.writeAsText(outputPath)

benv.execute()

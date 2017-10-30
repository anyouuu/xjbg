package dao

import scala.concurrent.{ ExecutionContext, Future }
import javax.inject.Inject

import models.Page
import play.api.db.slick.DatabaseConfigProvider
import play.api.db.slick.HasDatabaseConfigProvider
import play.db.NamedDatabase
import slick.jdbc.JdbcProfile
import slick.jdbc.MySQLProfile.api._

class PageDAO @Inject() ( protected val dbConfigProvider: DatabaseConfigProvider)(implicit executionContext: ExecutionContext) extends HasDatabaseConfigProvider[JdbcProfile] {
  import profile.api._

  private val Pages = TableQuery[PagesTable]

  def all(): Future[Seq[Page]] = db.run(Pages.result)

  def insert(page: Page): Future[Unit] = db.run(Pages += page).map { _ => () }

  private class PagesTable(tag: Tag) extends Table[Page](tag, "Page") {
    def id = column[Int]("id", O.PrimaryKey, O.AutoInc)
    def title = column[String]("title")
    def content = column[String]("content")

    def * = (id, title, content) <> (Page.tupled, Page.unapply)
  }
}

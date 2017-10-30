package controllers

import dao.CatDAO
import dao.DogDAO
import dao.PageDAO

import javax.inject._

import models._


import play.api.data.Form
import play.api.data.Forms.mapping
import play.api.data.Forms.text

import play.api.mvc._

//import scala.concurrent.ExecutionContext

import akka.actor.ActorSystem
import scala.concurrent.duration._
import scala.concurrent.{ExecutionContext, Future, Promise}


@Singleton
class DataController @Inject() (
                       catDao: CatDAO,
                       dogDao: DogDAO,
                       pageDao: PageDAO,
                       cc: ControllerComponents
                     )(implicit executionContext: ExecutionContext) extends AbstractController(cc) {

  def index = Action.async {
//    catDao.all().zip(dogDao.all()).map { case (cats, dogs) => Ok(views.html.data(cats, dogs)) }
    pageDao.all().map { case page => Ok(views.html.data(page)) }
//    Ok(views.html.data(pageDao.all()))
  }

  val catForm = Form(
    mapping(
      "name" -> text(),
      "color" -> text()
    )(Cat.apply)(Cat.unapply)
  )

  val dogForm = Form(
    mapping(
      "name" -> text(),
      "color" -> text()
    )(Dog.apply)(Dog.unapply)
  )

  var pageForm = Form(
    mapping(
      "id" -> text(),
      "title" -> text(),
      "content" -> text()
    )(Page.apply)(Page.unapply)
  )

  def insertCat = Action.async { implicit request =>
    val cat: Cat = catForm.bindFromRequest.get
    catDao.insert(cat).map(_ => Redirect(routes.DataController.index))
  }

  def insertDog = Action.async { implicit request =>
    val dog: Dog = dogForm.bindFromRequest.get
    dogDao.insert(dog).map(_ => Redirect(routes.DataController.index))
  }

  def insertPage = Action.async { implicit request =>
    val page: Page = pageForm.bindFromRequest.get
    pageDao.insert(page).map(_ => Redirect(routes.DataController.index))
  }
}

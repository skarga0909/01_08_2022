import logo from './logo.svg';
import './App.css';
import React from "react";
import AuthorList from "./components/Author";
import BookList from "./components/Books";
import NotFound404 from "./components/NotFound404";
import BooksAuthor from "./components/BooksAuthor";
import axios from "axios";
import {HashRouter, BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom';


class App extends  React.Component{
  constructor(props) {
    super(props)
    this.state = {
      'authors': [],
        'books': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/authors/').then(response =>{

       this.setState(
        {
          'authors':response.data
        }
    )
    }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/books/').then(response =>{

       this.setState(
        {
          'books':response.data
        }
    )
    }).catch(error => console.log(error))
  }

  render() {
    return (
      <div>
          <BrowserRouter>
              <nav>
                  <ul>
                      <li> <Link to='/'>Authors</Link></li>
                      <li> <Link to='/books'>Books</Link></li>
                  </ul>
              </nav>
              <Switch>
                  <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>} />
                  <Route exact path='/books' component={() => <BookList books={this.state.books} />} />
                  <Route path='/authors'>
                      <Route index element={<AuthorList authors={this.state.authors} />} />
                      <Route path=':authorId' element={<BooksAuthor books={this.state.books} />} />
                  </Route>
                  <Redirect from='/book' to='/books' />
                  <Route component={NotFound404} />
              </Switch>
          </BrowserRouter>
      </div>
    )
  }
}

export default App;

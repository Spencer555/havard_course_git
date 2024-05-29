import logo from './logo.svg';
import './App.css';
import Counter from './counter'
import Addition from './addition'

function Hello(props){
  return (
  <div>
     this is a test {props.name}
  </div>
)
}
function App() {
  return (
    <div className="App">
      fds
      <Hello name="red"/>
      <Hello name="blue"/>
      <Hello name="green"/>
      <Counter/>
      <Addition/>
    </div>
  );
}

export default App;

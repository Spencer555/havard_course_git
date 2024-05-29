import React from 'react'
import './Addition.css';

export default function Addition() {
    const [num1, setNum1] = React.useState(1);
    const [num2, setNum2] = React.useState(2);
    const [state, setState] = React.useState({
        num1:1, 
        num2:2,
        response: "",
        score:0,
        incorrect:false
    });
    function updateResponse(e){
        setState({
            ...state,
            response:e.target.value
        })
    }

    function inputonKeyDown(e){
        
        if (e.key === "Enter"){
            const answer = parseInt(state.response)
            if (state.num1 + state.num2 === answer){
                setState({
                    ...state,
                    num1:Math.ceil(Math.random() * 10),
                    num2:Math.ceil(Math.random() * 10),
                    score:state.score + 1,
                    response:'',
                    incorrect:false
                })
            } else {
                 setState({
                ...state,
                score:state.score - 1,
                response:'',
                incorrect:true,
               
            })}
        }
       
    }

    if (state.score === 10){
        return (
            <div id='done'>
                You Win
            </div>
        )
    }
    if (state.score < 0){
        return (
            <div id='done'>
                You Lose
            </div>
        )
    }
  return (
    <div>
     <hr />

      <div className={state.incorrect ? 'incorrect' : ''} id='problem'>{state.num1} + {state.num2}</div>
      <input onKeyDown={inputonKeyDown} onChange={updateResponse} value={state.response} autoFocus/>


      <div>Score: {state.score}</div>

    </div>
  )
}

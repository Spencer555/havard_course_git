import React, { useState } from 'react'

export default function Counter() {

  const  [count, setCount] = useState(0)

  const updateCount = () => {
    setCount(count + 1)
  }
    return (
    <div>
        <div>{count}</div>
        <button onClick={updateCount}>Count</button>
    </div>
   )
}

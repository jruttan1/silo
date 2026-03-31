import './index.css'
import { useEffect, useState } from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Landing from './pages/Landing.jsx'
import Notes from './pages/Notes.jsx'

function App() {
    const [theme, setTheme] = useState('fog')

    useEffect(() => {
        document.body.dataset.theme = theme
    }, [theme])

    return(
    <BrowserRouter>
        <Routes>
            <Route path = '/' element = {<Landing theme={theme} setTheme={setTheme}/>}/>
            <Route path = '/notes' element = {<Notes/>}/>
        </Routes>
    </BrowserRouter>
    
    )
}

export default App

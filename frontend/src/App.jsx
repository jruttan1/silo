import './index.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Landing from './pages/Landing.jsx'
import Notes from './pages/Notes.jsx'

function App() {
    return(
    <BrowserRouter>
        <Routes>
            <Route path = '/' element = {<Landing/>}/>
            <Route path = '/notes' element = {<Notes/>}/>
        </Routes>
    </BrowserRouter>
    
    )
}

export default App

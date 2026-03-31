import Hero from '../components/Hero.jsx'

function Landing({ theme, setTheme }) {
    return (
        <div>
            <Hero theme={theme} setTheme={setTheme}/>
        </div>
    )
}

export default Landing

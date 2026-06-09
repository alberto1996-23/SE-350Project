type HeaderProps = {
  leftImage: string
  rightImage: string
}

function Header({ leftImage, rightImage }: HeaderProps) {
  // I use this to render the restaurant branding at the top of the page.
  return (
    <header className="site-header">
      <div className="header-inner">
        <div className="chef-frame">
          <img src={leftImage} alt="Chef Pikachu" />
        </div>

        <div className="brand-block">
          <h1 className="brand-title">The Pika Joint</h1>
          <p className="brand-subtitle">A Pokémon-inspired restaurant</p>
        </div>

        <div className="chef-frame">
          <img src={rightImage} alt="Chef Eevee" />
        </div>
      </div>
    </header>
  )
}

export default Header
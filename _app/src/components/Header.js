import { Link } from 'gatsby'
import PropTypes from 'prop-types'
import React from 'react'

import Logo from './Logo'
import styles from './Header.module.css'

const Header = ({ siteTitle = '' }) => (
  <header className={styles.header}>
    <div className={styles.container}>
      <h1 className={styles.heading}>
        <Link to="/" className={styles.homeLink}>
          <Logo className={styles.logo} size={32} />
          {siteTitle}
        </Link>
      </h1>
    </div>
  </header>
)

Header.propTypes = {
  siteTitle: PropTypes.string,
}

export default Header

import sys
from time import sleep
from bullets import Bullet
from alien import Alien
import pygame


from bullets import Bullet

def check_events(ai_Settings,screen,stats, sb, play_button,ship,aliens,bullets):
    """Respons to events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ai_Settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            chack_play_button(ai_Settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_keydown_event(event,ai_Settings,screen,ship,bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_Settings,screen,ship,bullets)

def check_keyup_event(event,ship):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def updateScreen(ai_settings,screen,stats,sb,ship,aliens,bullets, play_button):
    """Update images on screen"""
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
    

    pygame.display.flip()

def update_bullets(ai_Settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()

    #Get Rid of the bullets when they disappeard
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(ai_Settings, screen, stats, sb, ship, aliens, bullets)

def fire_bullet(ai_Settings,screen,ship,bullets):
    """Fire bullets if limit not reched"""
    #Creating a new bullet and add it to group
    if len(bullets) < ai_Settings.bullets_allowed:
        new_Bullet = Bullet(ai_Settings,screen,ship)
        bullets.add(new_Bullet)

def create_fleet(ai_Settings,screen,ship,aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_Settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_Settings, alien_width)
    number_of_rows = get_number_aliens_y(ai_Settings,ship.rect.height,alien.rect.height)
 
    # Create the first row of aliens.
    for row_number in range(number_of_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            create_alien(ai_Settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_aliens_y(ai_settings,ship_height,alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3* alien_height) - ship_height)
    number_of_rows = int(available_space_y / (2 * alien_height))
    return number_of_rows
 
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height *  row_number
    aliens.add(alien)

def update_aliens(ai_Settings, screen, stats, sb, ship, aliens, bullets):
    """ Check if the fleet is at an edge,
    and then update the postions of all aliens in the fleet.
    """
    check_fleet_edge(ai_Settings, aliens) 
    aliens.update()

    #Look for alien and ship collsion
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_Settings, screen, stats, sb, ship, aliens, bullets)

    #Look for aliens hitting bottom of screen
    check_alien_bottom(ai_Settings, screen, stats, sb, ship, aliens, bullets)

def check_fleet_edge(ai_Settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_Settings,aliens)
            break

def change_fleet_direction(ai_Settings,aliens):
    """ Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_Settings.fleet_drop_speed
    
    ai_Settings.fleet_direction *= -1

def check_bullet_alien_collision(ai_Settings, screen, stats, sb, ship, aliens, bullets):
    #Check for any bullets that have hit the aliens
    #If so, then get rid of the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets,aliens,True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_Settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens)==0:
        #Destroy existing bullets and create new fleet.
        bullets.empty()
        ai_Settings.increase_speed()

        #Increase Level.
        stats.level+=1
        sb.prep_level()

        create_fleet(ai_Settings,screen,ship,aliens)

def ship_hit(ai_Settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to ship hit by alien"""

    if stats.ship_left > 0:
        #Decrement the number of ship
        stats.ship_left -= 1

        # Update scoreboard.
        sb.prep_ships()

        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the ship
        create_fleet(ai_Settings, screen, ship, aliens)
        ship.center_ship()

        #puse
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_alien_bottom(ai_Settings, screen, stats, sb, ship, aliens, bullets):
    """Cehck if any alien hit the bottom of screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treat this same as ship hit
            ship_hit(ai_Settings, screen, stats, sb, ship, aliens, bullets)
            break

def chack_play_button(ai_Settings,screen,stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start the new game if button clicked """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #Reset the game settings
        ai_Settings.initialize_dynamic_settings()
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        #Reset the game stats
        stats.reset_status()
        stats.game_active = True

        # Reset The scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #Empty the aliens and bullets
        aliens.empty()
        bullets.empty()


        #create a new fleet and center the ship
        create_fleet(ai_Settings, screen, ship, aliens)
        ship.center_ship()

def check_high_score(stats, sb):
    """Check to see if there is any new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

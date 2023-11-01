document.addEventListener('DOMContentLoaded', function () {
    const menuItems = document.querySelectorAll('.menu-item');

    menuItems.forEach(item => {
        const submenu = item.querySelector('.submenu');

        // Проверяем, есть ли подпункты
        if (submenu) {
            item.addEventListener('mouseover', () => {
                openSubmenu(item);
            });

            item.addEventListener('click', (event) => {
                if (event.target.tagName === 'A') {
                    // Перейти по ссылке при клике
                    return;
                }
                openSubmenu(item);
            });
        }
    });

    function openSubmenu(item) {
        const submenu = item.querySelector('.submenu');
        if (submenu) {
            submenu.style.display = 'block';
            closeOtherSubmenus(submenu);
        }
    }

    function closeOtherSubmenus(currentSubmenu) {
        menuItems.forEach(item => {
            const submenu = item.querySelector('.submenu');
            if (submenu && submenu !== currentSubmenu) {
                submenu.style.display = 'none';
            }
        });
    }
});
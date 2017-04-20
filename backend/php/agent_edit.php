<?php

public function agent_edit() {

        // get the agent from the get request
        $agent_id = trim($_GET['agent']);

        // get agent
        $agent = ( $agent_id == 'new') ? R::dispense('agent') : Models\Agent::load($agent_id);

        // check if agent is not set
        if ( !$agent ) {
            echo "agent not found";
            wp_die();
        }

        ?>

        <form name="agent-form" action="admin-ajax.php" method="post" id="agent-form">
            <input type="hidden" name="action" value="<?= self::ACTION_SAVE_AGENT ?>"><!-- Save action -->
            <input type="hidden" name="id" value="<?php echo (!empty($agent->id)) ? $agent->id : 'new'; ?>"> <!-- location id -->
        <div class="edit-wrap">
            <div class="alm-row">
                <div class="alm-button-row">
                    <!-- buttons go here -->
                    <?php
                    // return to admin page link
                    echo sprintf('<a class="button button-large" href="?page=%s">Back to Agent List</a>', ALM::ADMIN_PAGE);

                    ?>
                </div>
                <div class="alm-action-row">
                    <div class="alm-save-notice alm-small-flash-notice"></div>
                    <div class="alm-save-group">
                        <span class="spinner alm-spinner"></span>
                        <input class="button button-primary button-large alm-save-location-button" type="submit" value="Save" >
                    </div>
                    <?php
                    echo sprintf('<a class="button button-large" href="?page=%s">Cancel</a>', ALM::ADMIN_PAGE);
                    ?>
                </div>
            </div>

            <!-- spacer -->
            <div style="height:10px; width: 100%;"><br></div>

            <!-- notice -->
            <div id="alm-save-result" class="alm-large-flash-notice text-center text-bold"></div>

            <div class="alm-form-field">
                <h3><span><?php _e('Agent Details', ALM::TD); ?></span></h3>
                <div class="inside" >
                    <fieldset>
                        <div id="fname-error" class="input-error-notice alm-error-text"></div>
                        <label for="fname"><?php _e('First Name', ALM::TD);?>:</label>
                        <input id="fname" type="text" name="fname" placeholder="Agent FName" spellcheck="false" autocomplete="off" value="<?php if(!empty($agent->fname)) echo $agent->fname ?>"/>
                    </fieldset>

                    <fieldset>
                        <div id="lname-error" class="input-error-notice alm-error-text"></div>
                        <label for="lname"><?php _e('Last Name', ALM::TD);?>:</label>
                        <input id="lname" type="text" name="lname" placeholder="Agent LName" spellcheck="false" autocomplete="off" value="<?php if(!empty($agent->lname)) echo $agent->lname ?>"/>
                    </fieldset>

                    <fieldset>
                        <div id="id-error" class="input-error-notice alm-error-text"></div>
                        <label for="id"><?php _e('Agent ID', ALM::TD);?>:</label>
                        <input id="id" type="text" name="id" placeholder="Agent ID" spellcheck="false" autocomplete="off" value="<?php if(!empty($agent->id)) echo $agent->id ?>"/>
                    </fieldset>

                </div>
                <div class="inside" >
                    <fieldset>
                        <div id="email-error" class="input-error-notice alm-error-text"></div>
                        <label for="email"><?php _e('Email', ALM::TD);?>:</label>
                        <input id="email" type="text" name="email" placeholder="Email" spellcheck="false" autocomplete="off" value="<?php if(!empty($agent->email)) echo $agent->email ?>"/>
                    </fieldset>

                    <fieldset>
                        <div id="phone-error" class="input-error-notice alm-error-text"></div>
                        <label for="phone"><?php _e('Phone', ALM::TD);?>:</label>
                        <input id="phone" type="text" name="phone" placeholder="(555) 555-5555" spellcheck="false" autocomplete="off" value="<?php if(!empty($agent->phone)) echo $agent->phone ?>"/>
                    </fieldset>

                    <fieldset>
                        <div id="title-error" class="input-error-notice alm-error-text"></div>
                        <label for="title"><?php _e('Title', ALM::TD);?>:</label>
                        <input id="title" type="text" name="title" placeholder="Title" spellcheck="false" autocomplete="off" value="<?php if(!empty($agent->title)) echo $agent->title ?>"/>
                    </fieldset>

                    <fieldset>
                        <div id="photo-error" class="input-error-notice alm-error-text"></div>
                        <label for="photo"><?php _e('Agent Photo', ALM::TD);?>:</label>
                        <input id="photo" type="text" name="photo" placeholder="Photo URL" spellcheck="false" autocomplete="off" value="<?php if(!empty($agent->photo)) echo $agent->photo ?>"/>
                    </fieldset>

                </div>

            </div>

        </div>
        </form>

        <?php
        // get all agents
        $agents = Models\Agent::getAll();

        // don't include THIS agent
        if (isset($agent->id) && $agent->id) {
            unset($agents[$agent->id]);
        }
    }